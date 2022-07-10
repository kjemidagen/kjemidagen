import subprocess
from watchfiles import awatch
import pathlib
import asyncio

curr_path = pathlib.Path(__file__).parent.absolute().__str__()

async def main():
    print("Checking if server is already running")
    ls_result = subprocess.run(f"docker compose -f {curr_path}/docker-compose.yml ls -q", capture_output=True, text=True)
    if ls_result.stdout is None or "kjemidagen" not in ls_result.stdout:
        print("Starting server")
        subprocess.call(f"docker compose -f {curr_path}/docker-compose.yml up -d")
    else:
        print("Server is already running")
    print("Watching for file changes")
    async for changes in awatch(curr_path):
        frontend_changed = False
        backend_changed = False
        for change in changes:
            changed_path = pathlib.Path(change[1]).relative_to(curr_path)
            if (changed_path.parts[0] == "frontend"): 
                frontend_changed = True 
            if (changed_path.parts[0] == "backend"):
                backend_changed = True
        if frontend_changed:
            subprocess.run(f"docker compose -f {curr_path}/docker-compose.yml restart frontend")
        if backend_changed:
            subprocess.run(f"docker compose -f {curr_path}/docker-compose.yml restart backend")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        subprocess.run(f"docker compose -f {curr_path}/docker-compose.yml stop")
