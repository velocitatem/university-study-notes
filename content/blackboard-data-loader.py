from langchain.document_loaders import BlackboardLoader

loader = BlackboardLoader(
    blackboard_course_url="https://blackboard.ie.edu/ultra/courses/_42716_1/outline",
    bbrouter="expires:1681775951,id:2067BEFEB2332F469E19654BFB3119FA,signature:63edc8c112b683384cfbc51b060359e7e2eea6fc9f68973315a5818587707da2,site:1f72abaa-fb03-41c1-a1f5-ced024f53eaf,timeout:10800,user:e8c5f27882574e3485b64f07ca933b32,v:2,xsrf:347e6088-6112-466c-8170-a814d23caaf8",
    load_all_recursively=True,
)
documents = loader.load()
