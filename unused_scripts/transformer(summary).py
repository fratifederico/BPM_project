from transformers import pipeline

summarizer = pipeline("summarization", model="t5-base")

context = "The head of anti-monarchist campaign group Republic was arrested by police at a protest in Trafalgar Square before the Coronation of King Charles.Footage showed protesters in Not My King t-shirts being detained, including Republic's CEO Graham Smith.Six demonstrators, including Mr Smith, were stopped while unloading signs near the procession route, Republic said.The Metropolitan Police confirmed several arrests were made at demonstrations in the capital.The force said lock-on devices which protesters can use to secure themselves to things like railings - had been seized.But Republic said officers had misconstrued straps meant to secure their signs in place.Campaign groups and human rights groups criticised the incredibly alarming detentions, describing them as something you would expect to see in Moscow, not London."
summary = summarizer(context, max_length=100, min_length=10, do_sample=False)[0]["summary_text"]
print(summary)
