import subprocess
from watchfiles import awatch
import pathlib
import asyncio

curr_path = pathlib.Path(__file__).parent.absolute().__str__()

async def main():
    print("Watching")
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
            subprocess.call("docker compose restart frontend")
        if backend_changed:
            subprocess.call("docker compose restart backend")

if __name__ == "__main__":
    subprocess.call("docker compose up -d")
    asyncio.run(main())
