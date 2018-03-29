from tkinter import *
from tkinter import ttk
from geopy.geocoders import Nominatim
import MatPlot

import JobFile

mainWindow=Tk()#create a window

mainWindow.title("Job Notification in Bridgewater")

mainWindow.geometry('700x800')#setting the window size


jobInHtmlTag=JobFile.Job()#creating an object to get all job in html form from the the Job in the file JobFile


#from tkinter i am using the text widget to display the jobs
text=Text(mainWindow,font=28,height=700, width=800,highlightbackground="black")
label=Label(mainWindow,text="COMPUTER SCIENCE JOBS IN BRIDGEWATER",bg="red")#another title

#telling th user how to use the software
hint = Label(mainWindow,fg='blue',font="arial 14 bold")
hint2 = Label(mainWindow,fg='blue',font="arial 14 bold")
hint.config(text="TYPE IN A KEYWORD IN SEARCH BOX AND PRESS SEARCH BUTTON, EX JAVA")
hint2.config(text="MAKE SURE YOU CLOSE THE MAP BEFORE EACH SEARCH IN ORDER TO REFRESH IT")
hint.pack()
hint2.pack()


jobEntry = Entry(mainWindow, bd = 5)#entry for user to type the name of the location, they want to search


def getKeywordFromUser():
    jobLocation =jobEntry.get()#how you get the string from tkinter entry box
    return jobLocation

#when the user type a town follow by a state, this function will convert the string to long and lat and return them
#using geopy library
def getTownMeridians(townAndState):
    geolocator = Nominatim(scheme='http')
    meridians = geolocator.geocode(townAndState)
    return meridians#if town and state does not exit it returns none



'''def DisplayMap():
    townAdnState=getJobLocationFromUser()
    Long_Lat=getTownMeridians(townAdnState)
    #insertSpecificJobsToWidget(townAdnState)
    getJobByKeyword(townAdnState)
    if Long_Lat!=None and len(text.get("1.0", "end-1c"))>100:# if user enter a valid town then we diplay map
        map = MatPlot.Map(Long_Lat.longitude, Long_Lat.latitude, townAdnState)
        map.ShowMap()
        map.clearMap()'''

'''def displaymap(location):
    long_lat=getTownMeridians(location)
    #townAdnState = getJobLocationFromUser()
    # insertSpecificJobsToWidget(townAdnState)
    #getJobByKeyword(townAdnState)
    if long_lat != None and len(text.get("1.0", "end-1c")) > 100:  # if user enter a valid town then we diplay map
        map = MatPlot.Map(long_lat.longitude, long_lat.latitude, location)
        #map.ShowMap()
        #map.clearMap()'''


#this function removes the htlm tags text return the text without the tags in them
def refineHtmlTags(htmlTagToRefine):
    refinedTags=(htmlTagToRefine.replace("<p>","").replace("</p>","").replace("<strong>","").replace("</strong>","").replace("<span>","")
                .replace("</span>", "").replace("<br /><br />","\n").replace("<br />", "\n").replace("<br>", "").replace("<li>", "").replace("</li>", "")
                .replace("<ul>", "").replace("</ul>", "").replace("&bull", "").replace("&nbsp","").replace("&rsquo", "").replace("&amp","")
                .replace("&middot","").replace("<em>","").replace("</em>","").replace(";","").replace("<ol>","")
                .replace("</ol>","").replace("<blockquote>","").replace("</blockquote>","").replace("<sup>","").replace("<a>","").replace("</a>","")
                .replace("</sup>", "").replace("<a href","link "))
    return refinedTags

#this function get the jobs using userkeyword from user
def getJobByKeyword():
    location=[]#a list to save all location from each job that was returned by the user search
    map=None# a map that will be displayed
    keyword=getKeywordFromUser()
    if jobInHtmlTag.Connection != False:
        text.config(state="normal")
        text.delete('1.0', END)
        for specificJob in jobInHtmlTag.allJobs:
            if keyword.lower() in specificJob.title.string.lower() and len(keyword)!=0:
                title = specificJob.title.text.upper()
                description = refineHtmlTags(specificJob.description.text)
                text.insert(INSERT, title)
                text.insert(INSERT, "\n")
                text.insert(INSERT, description)
                text.insert(INSERT, "\n")
                text.insert(INSERT,
                            "----------------------------------------------------------------------------------------------------")
                text.insert(INSERT, "\n\n\n")
                location.append(specificJob.location.string)
        if len(location)>0:
            for town in location:
                long_lat = getTownMeridians(town)
                if long_lat != None and len(
                        text.get("1.0", "end-1c")) > 100:  # if user enter a valid town then we diplay map
                    map = MatPlot.Map(long_lat.longitude, long_lat.latitude, town)
        if map!=None:
            map.ShowMap()
            map.clearMap()

        if len(keyword) == 0:
            text.delete('1.0', END)
            text.insert(INSERT, " SEARCH BOX IS EMPTY, PLEASE TYPE THE JOB KEYWORD EX: JAVA")
        elif len(text.get("1.0", "end-1c")) == 0:
            text.insert(INSERT, " YOUR SEARCH DID NOT RETURN ANY RESULTS, CHECK SPELLING AND TRY AGAIN EX: BROCKTON MA")
    else:
        text.insert(INSERT, "YOU HAVE A PROBLEM WITH YOUR CONNECTION OR THE LINK")

    text.config(state="disabled")


#a button to be pressed after a user enter a search in the entry and that button also Display map
search = Button(mainWindow, text = "Search",font="Helvetica 16 bold", fg="blue", bd="1",command=getJobByKeyword)
search.place(x = 180,y = 50)


#giving the text to display the jobs some properties
text.config(wrap=WORD)
text.config(fg="blue")
text.config(bg="yellow")
text.insert(INSERT,"\n")





#this function take the text from the jobs and insert them into a text widget (Tkinter)
def insertJobsToWidget():#this one is manually tested. if text widget is not empty after insertng to it then it works
    text.config(state="normal")
    text.delete('1.0', END)#clear the text before inserting to it
    if jobInHtmlTag.Connection != False:
        for specificJob in jobInHtmlTag.allJobs:
            title = specificJob.title.text.upper()
            description = refineHtmlTags(specificJob.description.text)
            text.insert(INSERT, title)
            text.insert(INSERT, "\n")

            text.insert(INSERT, description)
            text.insert(INSERT, "\n")
            text.insert(INSERT,
                        "----------------------------------------------------------------------------------------------------")
            text.insert(INSERT, "\n\n\n")
    else:
        text.insert(INSERT, "YOU HAVE A PROBLEM WITH YOUR CONNECTION OR THE LINK")
    text.config(state="disabled")


'''def insertSpecificJobsToWidget(jobLocation):#this fucntion will return the jobs specified by the user
    if jobInHtmlTag.Connection != False:
        text.config(state="normal")
        text.delete('1.0', END)
        for specificJob in jobInHtmlTag.allJobs:
            if specificJob.location.string.replace(" ","").replace(",","").lower()==jobLocation.replace(" ","").replace(",","").lower():
                title = specificJob.title.text.upper()
                description = refineHtmlTags(specificJob.description.text)
                text.insert(INSERT, title)
                text.insert(INSERT, "\n")
                text.insert(INSERT, description)
                text.insert(INSERT, "\n")
                text.insert(INSERT,
                            "----------------------------------------------------------------------------------------------------")
                text.insert(INSERT, "\n\n\n")
        if len(getKeywordFromUser()) == 0:
            text.insert(INSERT, " SEARCH BOX IS EMPTY, PLEASE TYPE TOWN AND STATE EX: BROCKTON MA")
        elif len(text.get("1.0", "end-1c")) == 0:
            text.insert(INSERT, " YOUR SEARCH DID NOT RETURN ANY RESULTS, CHECK SPELLING AND TRY AGAIN EX: java")
    else:
        text.insert(INSERT, "YOU HAVE A PROBLEM WITH YOUR CONNECTION OR THE LINK")

    text.config(state="disabled")'''




def testForURLfound():
    return jobInHtmlTag.Connection

#a button to display all jobs
allJobs=Button(mainWindow, text = "See all",font="Helvetica 16 bold", fg="blue", bd="1",command=insertJobsToWidget)
allJobs.place(x = 465,y = 50)

jobEntry.pack()
text.pack()
mainWindow.mainloop()#to keep the prpgram running

