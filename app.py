import pandas as pd
import streamlit as st
import pickle
import regex as re
from urllib.parse import urlparse


#importing file
model = pickle.load(open("Model.pkl" , "rb"))


st.markdown("<h1 style='text-align: center;'>SecureSurf</h1>", unsafe_allow_html=True)


url = st.text_area(
    label = " ",
    max_chars = 1000,
    placeholder = "Drop URL here ..."
)


suspicious_keywords = [
    "login", "secure", "bank", "update", "free", "lucky", "bonus","urgent", 
    "alert", "verify", "confirm", "account", "action", "immediate","payment",
    "transfer", "credit", "loan", "invoice", "billing", "funds", "cash","win",
    "prize", "contest", "discount", "offer", "deal", "freegift","secure", 
    "safety", "protection", "security", "malware", "phishing","sign-in", 
    "logon", "access", "retrieve", "accountupdate","cheap", "freetrial",
    "bet", "casino", "adult","download", "file", "exe", "attachment", 
    "clickhere","signin"
]

def extract_features(url):
    features = {}

    ## Length of domain 
    domain = urlparse(url).netloc
    if re.match(r"^www.", domain):
        domain = domain.replace("www.", "")    
    features["domain_length"] = len(domain) if domain else 0

    ## TLD (Top Level Domain)
    tld_match = re.search(r'[^.]+$', domain)
    tld = tld_match.group(0) if tld_match else None 
    features["tld_length"] = len(tld) if tld else 0

    ## Check whether URL is HTTPS or HTTP
    features["is_HTTP"] = 0 if re.match(r"^https:?//", url) else 1   

    ## Check if URL is in the form of IP address
    features["is_IP"] = 1 if re.match(r"^(\d{1,3}\.){3}\d{1,3}$", url) else 0

    ## Count number of Subdomains
    domain_parts = domain.split('.')
    features["no_of_Subdomains"] = len(domain_parts) - 2 if len(domain_parts) > 2 else 0

    ## Depth of URL
    path = urlparse(url).path
    depth = len([segment for segment in path.split('/') if segment])
    features["url_depth"] = depth

    ## Checking for redirection
    pos = url.rfind("//")
    if pos > 6:
        features["redirection"] = 1
    else:
        features["redirection"] = 0

    ## Check if URL contain "@" symbol
    features["contain_@"] = 1 if "@" in url else 0
    
    ## Check if URL contain "-" symbol
    features["contain_hyphen"] = 1 if "-" in url else 0

    ## Check whether URL contain any suspicious keywords
    features["contains_suspicious_keywords"] = 1 if any(keyword in url.lower() for keyword in suspicious_keywords) else 0

    return features


def endpoint(url):
  features = pd.Series(extract_features(url))
  features_df = pd.DataFrame([features])
  result = model.predict(features_df)[0]
  return result

style = "<style>.row-widget.stButton {text-align: center;}</style>"
st.markdown(style, unsafe_allow_html=True)

if st.button("Predict"):
  result = endpoint(url)
  if result == 1:
    st.success("Update: The URL is legitimate.")
  else:
    st.warning("Warning!!! The URL is a phishing attempt.")
