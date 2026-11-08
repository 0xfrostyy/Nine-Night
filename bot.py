import asyncio
from playwright.async_api import async_playwright, TimeoutError


ANSWER = "C"

accounts = [
   


{"username":"S2G-51","wallet":"97wsj5RAvpPhfzXSVc9TqnhM4jm1gg5zTBtdYSgKFXzA"},
{"username":"S2G-52","wallet":"BFB1fLmHCftXzax6zVYMdSxq8QxMRhsL6P2WcHP3xuky"},
{"username":"S2G-53","wallet":"2sMtSZRFREH7ytXmmiBSmhjixd5zM4ig9S4A2sDWufb8"},
{"username":"S2G-54","wallet":"GEUVKJ3VHTxvy6rWEW9CKC59nMUf56Xm516pvevgQRL5"},
{"username":"S2G-55","wallet":"6KopzoMwXZqVeQqKQjTd7r7ST8CZBAi5AeTNzDpbWEK9"},
{"username":"S2G-56","wallet":"2fEkawCiA5c2Lf7iu4K8rkkaRCqsWi8rxtJ5sqB2hYEk"},
{"username":"S2G-57","wallet":"2JYtusVBNaUjzBvKHo7Dn63EoAsedoocNBsXcFRendEz"},
{"username":"S2G-58","wallet":"AgXDE2Ro8uxTrjMEbK8LPe9tKEdnTFmU9euBAnP1R6Dm"},
{"username":"S2G-59","wallet":"9qfUJNnYXVNQQyoegAZQXvCugUdAe8LpcPbVW3nvLdFH"},
{"username":"S2G-60","wallet":"21mRdmiyQ92oWBJfoUyJAccpZ5H1fkfZmjLXrBk5NCkz"},



  
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

               await page.wait_for_timeout(10)
            await context.close()

           
            await context.close()

        await browser.close()
        print("🎉 All accounts processed successfully!")

if __name__ == "__main__":
    asyncio.run(run_bot())
