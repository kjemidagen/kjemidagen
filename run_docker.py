import subprocess
from watchfiles import awatch
import pathlib
import asyncio

curr_path = pathlib.Path(__file__).parent.absolute().__str__()

async def main():
    ls_result = subprocess.run("docker compose ls -q", capture_output=True, text=True)
    if ls_result.stdout is None or "kjemidagen" not in ls_result.stdout:
        subprocess.call("docker compose up -d")
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
            subprocess.run("docker compose restart frontend")
        if backend_changed:
            subprocess.run("docker compose restart backend")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        subprocess.run("docker compose stop")
