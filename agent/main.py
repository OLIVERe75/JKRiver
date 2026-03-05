
from datetime import datetime
from agent.config import load_config
from agent.config.prompts import get_labels
from agent.core import SessionManager, run_cycle, run_cycle_async
import asyncio
from agent.storage import load_current_profile

def _print_log(level: str, msg: str):
    pass

def _print_cycle_details(result: dict, CL: dict):
    reply = result.get("response", "")
    if reply:
        print(reply)

def _check_llm_reachable(config: dict):
    """Warn if the configured LLM backend is not reachable."""
    import requests
    llm = config.get("llm", {})
    api_base = llm.get("api_base", "")
    if not api_base:
        return
    try:
        requests.get(api_base, timeout=5)
    except Exception:
        provider = config.get("llm_provider", "local")
        if provider == "local":
            print(f"⚠ Cannot reach Ollama at {api_base}")
            print("  Please run 'ollama start' first, then try again.")
        else:
            print(f"⚠ Cannot reach LLM API at {api_base}")

async def main_async():
    config = load_config()
    _check_llm_reachable(config)
    CL = get_labels("cli.labels", config.get("language", "zh"))
    manager = SessionManager(config)
    session = manager.get_or_create()

    profile = load_current_profile()

    try:
        while True:
            user_input = input("> ")
            if user_input.strip().lower() == "quit":
                break
            if not user_input.strip():
                continue
            result = await run_cycle_async(user_input, session, log_fn=_print_log)
            _print_cycle_details(result, CL)
    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        from agent.sleep import run_async as sleep_run_async
        await sleep_run_async()

def main():
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
