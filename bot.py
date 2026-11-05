import asyncio
from playwright.async_api import async_playwright, TimeoutError


ANSWER = "B"

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
{"username":"S2G-61","wallet":"HQhHKftPce8J6qkytLb9mz3sCPr6RvBn1AHW448PsQP4"},
{"username":"S2G-62","wallet":"Hbpf49afXJskVJkZY2D276m6iA4inMgFfc8jL98bXgHz"},
{"username":"S2G-63","wallet":"Crhsm3dzngwuQuWFKNBGPzAZoP8pVdG8hWj8KRrg8npM"},
{"username":"S2G-64","wallet":"DNvJsH7LFDQXcnD1smk7iU68NLctyD7wAxp6Ri6wbLhC"},
{"username":"S2G-65","wallet":"611cuPQtWdiKxveNwb91iefoXfRkyzrDFbTEdYzakDfk"},
{"username":"S2G-66","wallet":"FFYGG71bdRHK5u6Bx52oRa25seS2WQbQmLDTMNbYPJaD"},
{"username":"S2G-67","wallet":"B3apxLs57H9iggU1sj4j8gsu5mRASyw2FfGq2LEYieVD"},
{"username":"S2G-68","wallet":"A9dbGojLg39yZeZgAU52f7pHxDPAQusFEabBxGCpVpBx"},
{"username":"S2G-69","wallet":"8CNrfLF57MMyQN68TwgvkGDiNxtW9wZRWhcWUcpmMVjP"},
{"username":"S2G-70","wallet":"8nqK5nQhidTTZAGETR9GKB16wWQkvTw8dZDMY6nzFThk"},
{"username":"S2G-71","wallet":"2nWoNGE1pAYyBKn93Pv5p36rapnUMEZ1LdQj7YahVHgo"},
{"username":"S2G-72","wallet":"6vWbeXbSu3EwKAJ278d94xRgXREwBJ51vZXFBF8CZsCg"},
{"username":"S2G-73","wallet":"G3PQAaFCr9FxG9cp2xNUS6dDgD5jk9LkcnyKWwserh6M"},
{"username":"S2G-74","wallet":"7mt3QKdqVZmdcr9NE7ztp6Sv2tEpyGZxXGmznU28o77a"},
{"username":"S2G-75","wallet":"Gw5DNjGib6vzL4oT1AsUAoR1FmeGdGiw6RmRNtqnJ6Z7"},
{"username":"S2G-76","wallet":"BRwhawrTHr9Dfm2UyND5CZh8YM2Bm6MYhvPqQMj5XREv"},
{"username":"S2G-77","wallet":"X5i2WtpNEdGzkwraEq8NkTWUj9on1XfmaDEsUMNeEDj"},
{"username":"S2G-78","wallet":"AinFw9as1Ts6qf4KZGKF1eTNWBkXZVBLokJd3QPK7T85"},
{"username":"S2G-79","wallet":"EwNkRJo4WV934GF6DZiVqCZA3AXnETFzYVPGMhL6dZSQ"},
{"username":"S2G-80","wallet":"HFkS7EfvBR1X5ogNQqVudByQx3c8R6GWgeZYF9VWK5Ca"},
{"username":"S2G-81","wallet":"5QX9MgHCteHDQVuzetG23Bd1a6FSi6LtfVKAkdEtyP8S"},
{"username":"S2G-82","wallet":"FSNtZKjbP2hgPZcDPQbgg3Nca4pKi2BnAE4qW2hn9wV9"},
{"username":"S2G-83","wallet":"82MnzMHX6BcA4rU7b2RKRogcKSxSuTXW3B9BcKkH7Jan"},
{"username":"S2G-84","wallet":"C1cARio9XvVPSzKLczvF9ogMsbXQTxvCWcafFB7HtYsv"},
{"username":"S2G-85","wallet":"GLFkD6TwUim1pQpCQPEkrkr13KnLNyxUEsgQaFzv7puB"},
{"username":"S2G-86","wallet":"Da3YCeQDD3rJVMNHFPyJzra9FRJ953qXs8p2Pw7L4VbX"},
{"username":"S2G-87","wallet":"4kdZvU9RuTuaN4cZsfngxFpSvoFt55oe7yHhPVJdHr4y"},
{"username":"S2G-88","wallet":"3cFEYKPmmT8N4Sm73pTrUb8RT7dC1MxRBufmEbf8XnPF"},
{"username":"S2G-89","wallet":"CQ6J77APkHrQw51YAhZZw4e21GHUzaXXQ2x9ypALmXcg"},
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
