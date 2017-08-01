import aiml


mybot = aiml.Kernel()

mybot.setBotPredicate('name','myBot')
mybot.setBotPredicate('botmaster','Sascha')

mybot.learn('aiml/sample.aiml')
mybot.saveBrain('aiml.brn')

sessionId = 12345

while True:
    s = input("Ask me anything: ") 
    if s == "sair":
        sys.exit(0)
    
    response = mybot.respond(s, sessionId) 
    autor = mybot.getPredicate('autor', sessionId)
    print(autor)    
    print ('Zeus: ', response)
