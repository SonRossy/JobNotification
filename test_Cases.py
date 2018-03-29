import pytest
from geopy.geocoders import Nominatim
import MainFile
from unittest.mock import patch
from tkinter import *



def test_refineHtmlTags():#test if the function removes the tags html markup
    assert "refined tag"==MainFile.refineHtmlTags("<p><p>refined <a>tag<p></p>")

@pytest.mark.xfail
def test_testForURLnotfound():#expect to fail if connection is successfull
    assert MainFile.jobInHtmlTag.Connection==False


@pytest.mark.xpassed
def test_testForURLfound():#expect to pass if connection is successfull and fail if not
    assert MainFile.jobInHtmlTag.Connection==True

#i am using a librarry called geopy which needs to be installed in order to pass ths test
#i am testing for one town if i get its lattiude ang longitude, i googled brockton meridians and test for it with my function
def test_getTownMeridians():
    Long_lat=MainFile.getTownMeridians("Brockton Ma")
    assert (Long_lat.longitude, Long_lat.latitude)==(-71.0183787 ,42.0834335)

#assuring the function return different meridians when provided different town
def test_getTownMeridians2():
    Long_lat=MainFile.getTownMeridians("Boston Ma")
    assert (Long_lat.longitude, Long_lat.latitude)!=(-71.0183787 ,42.0834335)

@patch('MainFile.getKeywordFromUser()',return_value="java")
def test_getJobLocationFromUser(getJobLocationFromUser):
    assert MainFile.getKeywordFromUser()=="java"
