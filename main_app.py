import streamlit as st
import joblib

def main() :
    vectorizer = joblib.load('data/Yelp_vectorizer.pkl')
    classifier = joblib.load('data/Yelp_classifier.pkl')

if __name__ == '__main__' : main()