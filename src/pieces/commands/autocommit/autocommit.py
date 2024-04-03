import os
    model = commands_functions.model_id
    message_prompt = f"""Act as a git expert developer to generate a concise git commit message **using best git commit message practices** to follow these specifications:
                `Output format WITHOUT ADDING ANYTHING ELSE: message is **YOUR COMMIT MESSAGE HERE**`",
                `Note: Don't generate a general commiting message make it more relevant to the changes`.
                `Here are the changes summary:`\n{changes_summary}"""
    issue_prompt = """Please provide the issue number that is related to the changes, If nothing related write 'None'.
                    `Here are the issues:`\n{issues}"""
        commit_message = pos_client.QGPTApi(api_client).relevance(
            pos_client.QGPTRelevanceInput(
                query=message_prompt,
                paths=[os.getcwd()],
                application=commands_functions.application.id,
                model=model,
                options=pos_client.QGPTRelevanceInputOptions(question=True)
            )).answer.answers.iterable[0].text
        
            issue_list = "\n".join(issue_list) # To string
            try:
                
                issue_number = commit_message = pos_client.QGPTApi(api_client).relevance(
                        pos_client.QGPTRelevanceInput(
                            query=issue_prompt.format(issues=issue_list),
                            paths=[os.getcwd()],
                            application=commands_functions.application.id,
                            model=model,
                            options=pos_client.QGPTRelevanceInputOptions(question=True)
                        )).answer.answers.iterable[0].text
        
                
