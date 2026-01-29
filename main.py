import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

def main():
    load_dotenv()
    console = Console()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) < 2:
        console.print("[bold red]Usage:[/bold red] python main.py <prompt>")
        sys.exit(1)
    prompt = sys.argv[1]

    verbose_flag = False
    if len(sys.argv) > 2:
        if sys.argv[2] == "--verbose":
            verbose_flag = True

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]

    with console.status("[bold green]Generating response...[/bold green]"):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction="You are a helpful assistant. Answer as a markdown format. Be concise and friendly."),
            contents=messages,
        )

    if response.text:
        console.print(Markdown(response.text))
    
    if verbose_flag:
        console.print("\n" + "-" * 20)
        if response is None or response.usage_metadata is None:
            console.print("[yellow]Usage metadata not available[/yellow]")
        else:
            metadata = response.usage_metadata
        console.print(Panel(
            f"[bold blue]Prompt Tokens:[/bold blue] {metadata.prompt_token_count}\n"
            f"[bold blue]Response Tokens:[/bold blue] {metadata.candidates_token_count}\n"
            f"[bold blue]Total Tokens:[/bold blue] {metadata.total_token_count}",
            title="Usage Metadata",
            expand=False
        ))


if __name__ == "__main__":
    main()
