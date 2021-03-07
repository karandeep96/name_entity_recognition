import streamlit as st
import spacy_streamlit
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
import wikipediaapi



def getPage(page_name):
	wiki_wiki = wikipediaapi.Wikipedia(
		language='en', 
		extract_format=wikipediaapi.ExtractFormat.WIKI
		)
	page_name = page_name.replace(" ", "_")
	page_py = wiki_wiki.page(page_name)
	if(page_py.exists()):
		page_text = page_py.text
		return page_text
	else:
		print("Enter Correct Page Name")

def getNER(page_text):
	nlp = en_core_web_sm.load()
	doc = nlp(page_text)
	
	
	return displacy.render(nlp(str(doc)), jupyter=True, style='ent')
	

st.title('Welcome to Named Entity Recognition')
st.header("Let's see Named Entity Recognition in action")







#@st.cache(suppress_st_warning=True)
def main(name):
	page_text = getPage(name)
	nlp = en_core_web_sm.load()
	doc = nlp(page_text)
	spacy_streamlit.visualize_ner(doc,labels=nlp.get_pipe('ner').labels)
	
	
	
if __name__=="__main__":
	name = st.text_input("Enter the name of Wikipedia Page", 'Google')
	main(name)
