def build_prompt(
    role: str,
    task: str,
    user_input: str,
    constraints: list[str] | None = None,
) -> str:                    #-> is mean the output should be string type 

    constraints_text = ""   #عشان بعدين نحط فيه الـ constraints لو موجودة.

    if constraints:
        constraints_text = "\n".join( f"- {item}"  for item in constraints )

    return f"""
            Role:
            {role}

            Constraints:
            {constraints_text}

            Task:
            {task}

            Input:
            <input>
            {user_input}
            </input>
                """.strip()    # delete the spaces between words in the first and the last only 