from InquirerPy import prompt
import pyttsx3
import speech_recognition as sr 






def todo_list_run():

    engine = pyttsx3.init()
    recognizer = sr.Recognizer()

    todo_list = []
    condition = True


    # SPEAKING FUNCTION
    def speak(text):
        engine.say(text)
        engine.runAndWait()

    # Listern Function
    def listen_command():

        try :
            
            with sr.Microphone() as source:
                print("Listening for command...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            command = recognizer.recognize_google(audio)
            print(f"Recognize Command : {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I am having trouble accessing the speech service.")
            return ""
        except Exception as e:
            print(f"Error: {e}")
            return ""


    def add_task():
            
            
            try:
                speak("What task would you like to add?")
                task = listen_command()
                if task:
                        
                    todo_list.append(task)
                    print(f"Task added: {task}")
                    speak(f"Task added: {task}")
                    return False
                else:
                    speak("No task was added.")
            except Exception as e:
                print(f"Error adding task: {e}")



    def delete_task():
        
        if not todo_list:
            speak("No tasks to delete.")
            return
        delete_task_prompt = [{
            "type": "list",
            "name": "task_to_delete",
            "message": "Select a task to delete:",
            "choices": todo_list
        }]
        delete_answer = prompt(delete_task_prompt)
        todo_list.remove(delete_answer["task_to_delete"])
        print(f"Task deleted: {delete_answer['task_to_delete']}")
        speak(f"Task deleted: {delete_answer['task_to_delete']}")


    def view_tasks():
        
        if not todo_list:
            speak("No tasks available.")
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            speak("Here are your current tasks.")
            for i, task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
                speak(f"Task {i}: {task}")

    while condition:
        speak("Please say a command: Add task, Delete task, View tasks, or Exit.")
        command = listen_command()


        if "add task" in command:
            add_task()
        elif "delete task" in command:
            delete_task()
        elif "view task" in command:
            view_tasks()
        elif "exit" in command:
            speak("Exiting the to-do list.")
            condition = False
        else:
            speak("Command not recognized. Please try again.")

if __name__ == "__main__":
    todo_list_run()