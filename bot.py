import asyncio
from playwright.async_api import async_playwright, TimeoutError


ANSWER = "B"

accounts = [
   


{"username":"S2G-90","wallet":"7KE8cawR7hB2s7sd1kKTz6N1kphPuXGQfcJfnhYdgP48"},
{"username":"S2G-91","wallet":"HDLeVS64fGNdEMRG3DRBW5wUn3oXNMWe8pYLrxKbMit"},
{"username":"S2G-92","wallet":"8M1vs4CpkpueDLqUdYm425FZe4TiZjFA5D5BcR5sfncu"},
{"username":"S2G-93","wallet":"AyKQCxCA6ZwXrVtgUcMoNAV3iPR4WXbHoLR35STQtfcS"},
{"username":"S2G-94","wallet":"Hz9kZihwHv7Tiz8zVPmYKmCS7MW5XvVnsUiCnW2jfu9P"},
{"username":"S2G-95","wallet":"9nxCrwY1HaTz7H1J5WPAUqKnapxEFwStU1S5Bgi8FoCJ"},
{"username":"S2G-96","wallet":"5KMFf4EGUB644sXQS63CvLp2ZZev3Z1rkawk1oBMnVgy"},
{"username":"S2G-97","wallet":"4CJgsxLWLeFjZoWaJv1g9BbuV3HehhLUkb6csNGMA1gf"},
{"username":"S2G-98","wallet":"FVRsb2QFZB4Ra5PPt7FQ7RHQZF6JXW6fbEnc2RZDe92L"},
{"username":"S2G-99","wallet":"HDBRgqQE2rAhhPuK5WZ2zU2dSJpTLran2K5AQsvyZods"},
{"username":"S2G-100","wallet":"EYo9TCCE184SAHbEesw5FYttrFjhhcWePxaMcCxhNBX5"},

  
]

async def handle_modal(page):
    modal = page.locator("#scamMigrationWarningModal")
    try:
        if await modal.is_visible(timeout=5000):
            print("⚠️ Closing modal...")
            buttons = modal.locator("button")
            if await buttons.count() > 0:
                await buttons.first.click()
                await page.wait_for_timeout(1000)
    except:
        pass

async def run_bot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        for acc in accounts:
            context = await browser.new_context()
            page = await context.new_page()

            print("Running account:", acc["username"])

            try:
                await page.goto("https://theros.io/prelaunch", timeout=80000)
                await page.wait_for_load_state("networkidle", timeout=15000)
            except TimeoutError:
                print(f"Timeout for {acc['username']}. Skipping.")
                await context.close()
                continue

            await handle_modal(page)
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_selector("input", timeout=15000)

            inputs = await page.query_selector_all("input")
            if len(inputs) < 2:
                print(f"Not enough inputs for {acc['username']}, skipping")
                await context.close()
                continue

            await inputs[0].fill(acc["username"])
            await inputs[1].fill(acc["wallet"])

            if len(inputs) > 2:
                await inputs[2].fill("bot")

            await handle_modal(page)

            create_btn = page.locator("#registerBtn")
            try:
                await create_btn.click(timeout=9000)
            except TimeoutError:
                await create_btn.click(force=True)

            next_btn = page.locator("#nextQuestionBtn")
            try:
                await next_btn.wait_for(state="visible", timeout=8000)
                await next_btn.click()
            except:
                pass

            answer_selector = f"#answer{ANSWER.upper()}"
            try:
                await page.locator(answer_selector).click(timeout=20000)
                print("Answered:", ANSWER)
            except Exception as e:
                print(f"Failed to answer: {e}")

            await context.close()

        await browser.close()
        print("🎉 All accounts processed successfully!")

if __name__ == "__main__":
    asyncio.run(run_bot())
