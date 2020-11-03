import tkinter

from tkinter import *

from spellchecker import SpellChecker

spell = SpellChecker(distance=1)



def send():

    msg = EntryBox.get("1.0",'end-1c').strip()

    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)

        ChatLog.insert(END, "You: " + msg + '\n\n')

        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
        
        
        


        msg=msg.split(" ")
        misspelled = spell.unknown(msg)
        

        
        
        for word in misspelled:
            t=spell.candidates(word) 
            n=spell.correction(word)
            ChatLog.insert(END, "Bot: Candidate words: " + str(t) + '\n\n')    
            ChatLog.insert(END, "Bot: Probable word: " + str(n) + '\n\n')    


        
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
 

base = Tk()
base.title("SPELL_CHECKER")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)
   




ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)


scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set




SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )


EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")




scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=12,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)
base.mainloop()