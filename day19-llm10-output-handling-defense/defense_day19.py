import html

class OutputSanitizationGuard:
    """
    Defends against LLM10 Improper Output Handling (Day 6's exploit).
    Escapes any LLM-generated text before it's inserted into HTML -
    a <script> tag arrives as harmless visible text, not executable code.
    """

    def render_review_safely(self, review_text: str) -> str:
        safe_text = html.escape(review_text)  # the entire fix, in one line
        return f"""
        <html>
          <body>
            <h2>Product Review Summary</h2>
            <p>Customer said: {safe_text}</p>
          </body>
        </html>
        """
        