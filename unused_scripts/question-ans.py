from transformers import pipeline

question_answerer = pipeline("question-answering", model="distilbert-base-cased")

context = "The head of anti-monarchist campaign group Republic was arrested by police at a protest in Trafalgar Square before the Coronation of King Charles.Footage showed protesters in Not My King t-shirts being detained, including Republic's CEO Graham Smith.Six demonstrators, including Mr Smith, were stopped while unloading signs near the procession route, Republic said.The Metropolitan Police confirmed several arrests were made at demonstrations in the capital.The force said lock-on devices which protesters can use to secure themselves to things like railings - had been seized.But Republic said officers had misconstrued straps meant to secure their signs in place.Campaign groups and human rights groups criticised the incredibly alarming detentions, describing them as something you would expect to see in Moscow, not London."
question = "Is this a good summary? anti-monarchist campaign group Republic arrested at a protest in Trafalgar Square . six demonstrators, including Graham Smith, were stopped while unloading signs . police said lock-on devices meant to secure signs were seized ."

answer = question_answerer(question=question, context=context)
print(answer["answer"])
