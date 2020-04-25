import streamlit as st
import random
import string
import time
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# text for comparison: sonnet_xviii
with open('/home/james/monkeys/sonnet18.txt', 'r') as f_open:
    sonnet_xviii = f_open.read()

#images
image_one = Image.open('/home/james/monkeys/chimptyping.jpg') 
image_two = Image.open('/home/james/monkeys/surprise.jpg')
image_three = Image.open('/home/james/monkeys/typewriter.jpg')


# BEGIN SIDEBAR

st.sidebar.markdown(":see_no_evil::hear_no_evil::speak_no_evil:")
st.sidebar.subheader("Set Up Your Simulation:")

# sidebar inputs
monkeys = st.sidebar.number_input('How Many Monkeys?', 1, 1000000, 1000, 1)
years = st.sidebar.slider('Typing for how many years?', 1, 3000, 1000, 1)
speed = st.sidebar.slider("How fast do your monkeys type?", .01, 216.0, 40.0)

# counters for each selection
st.sidebar.markdown("**Your settings: **")
st.sidebar.markdown(":date:: " + "**" + str(years) + " Years**")
st.sidebar.markdown(":monkey_face:: " + "**" + str(monkeys) + " Monkeys**" )
st.sidebar.markdown(":keyboard:: " + "**" + str(speed) + " WPM**" )

start_sim = False

if st.sidebar.button('Start your simulation'):
    start_sim = True
    
st.sidebar.markdown("-------------------------")

st.sidebar.subheader("Bonus:")

monkeying_around = st.sidebar.markdown(":banana:")

if st.sidebar.button("Feed a monkey a banana?"):
    	monkeying_around.markdown(":banana:_____________:monkey:")
    	time.sleep(0.3)
    	monkeying_around.markdown(":banana:___________:monkey:")
    	time.sleep(0.3)
    	monkeying_around.markdown(":banana:__________:monkey:")
    	time.sleep(0.3)
    	monkeying_around.markdown(":banana:_________:monkey:")
    	time.sleep(0.3)
    	monkeying_around.markdown(":banana:________:monkey:")
    	time.sleep(0.3)
    	monkeying_around.markdown(":banana:_______:monkey:")
    	time.sleep(0.3)
    	monkeying_around.markdown(":banana:_____:monkey:")
    	time.sleep(0.3)
    	monkeying_around.markdown(":banana:___:monkey:")
    	time.sleep(0.3)
    	monkeying_around.markdown(":banana::monkey:")
    	st.balloons()
    	monkeying_around.markdown(":monkey:")
    	if random.randint(1,2) == 2:
	    	time.sleep(3)
	    	monkeying_around.markdown(":monkey::poop:")
    	else:
	    	monkeying_around.markdown(":monkey:")


st.sidebar.markdown("-------------------------")
st.sidebar.markdown("*Version 0.1.4*")

# END SIDEBAR

# DEFINE VARIABLES
# calculate the total number of characters the monkeys can enter
monkey_business  = monkeys * years * speed
monkey_business *= 5 #WPM assumes 5 characters per word
monkey_business *= 525600 #minutes in a year

# calculate the number of sonnets to create
sonnet_length = len(sonnet_xviii)
sonnet_number = monkey_business / sonnet_length

# source for randomly generated text
chars = "134567890-=!&*()_+qwertyuiop{}QWERTYUIOP[]\\asdfghjkl;'ASDFGHJKL:\"zxcvbnm,./ZXCVBNM<      >?" # spacebar is bigger...so extra spaces?
chars_len_less = (len(chars) -1)

def sonnet():
    	random_sonnet = ""
    	for i in range (sonnet_length):
    	    	random_sonnet += chars [random.randint(0, chars_len_less)]
    	st.subheader("Sonnet " + str(format(random.randint(1,int(sonnet_number)), ",d")) + " by Monkey Shakespeare #" + str(random.randint(1,monkeys)))
    	st.write(random_sonnet)
    	st.markdown("-------------------------")


# MAIN DISPLAY BEGIN
st.title('The Infinite Monkey Theorem Simulator')
st.header("What is the 'Infinite Monkey Theorem?'")
st.write('"The infinite monkey theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of time will almost surely type any given text, such as the complete works of William Shakespeare." - [Wikipedia](https://en.wikipedia.org/wiki/Infinite_monkey_theorem)')


# progress bar
latest_iteration = st.empty()
bar = st.progress(0.0)

if start_sim:
    for i in range(99):
    	# Update progress bar with each iteration
    	latest_iteration.text('Your monkeys are busy typing...')
    	bar.progress(i+1)
    	time.sleep(0.02)
    latest_iteration.text(f'Your monkeys have been busy...')
    done = st.empty()

    x = np.arange(years)
    x_label =[]
    for year in range(2020, (2020 + years)):
    	x_label.append(year)
    y = []
    ws = []
    for year in range(1,(years+1)):
    	y.append(int(round(((sonnet_number / years)*year),0)))
    	ws.append(int(152))

    # display a bar chart of the sonnets the monkeys made
    plt.bar(x, y, color="red", log=0, label ="Monkeys")
    plt.ylabel("Sonnets")
    plt.title("Cumulative Monkey Sonnets (2020 - " + str((2020+years)) + ")" )
    plt.xlabel("Year")
    #plt.legend()
    st.pyplot()
    bar.progress(100)
    st.balloons()
    done.text('...and now they\'re done!')


    st.write("You had " + str( monkeys) + " monkeys typing, for " + str(years) + " years, at " + str(speed) + " WPM.")
    st.write("Your mighty monkeys hit the keys approximately " + str(format(int(monkey_business), ",d")) + " times.")
    st.write("That means they wrote you " + str(format(int(sonnet_number), ",d")) + " sonnets. Wow! Nice work, monkeys!")

    st.image(image_one, use_column_width=True, caption="New York Zoological Society / Public domain")

    st.write("Sadly, even with years of practice, most of your monkeys' sonnets are kind of terrible...")
    st.write("But you can judge for yourself. Check out a sample of their work below.")

    st.markdown("-------------------------")

    for i in range(3):
    	sonnet()

    st.subheader("Still, these monkeys probably deserve a banana for their all their hard work though, don't do you think?")
    st.image(image_two, use_column_width=True, caption="Did someone say Banana? (Photo by Jamie Haughton on Unsplash)")
    st.subheader("There's a button on the sidebar to feed a monkey a banana.")

    st.markdown("*Note: If you click the button in the sidebar to feed the monkey, it will clear your simulation.*")
else:
    	st.subheader("Use the sidebar on the left to set up the monkey simulation and then get ready to see what your monkeys write.")
    	st.image(image_three,use_column_width=True, caption="Photo by Matt Artz on Unsplash")
    	st.markdown("-------------------------")

st.header("Can a thousand monkeys typing for a thousand years write one of Shakespeare's sonnets?")
st.write("Some say that over an infinite time or infinite  monkeys it's bound to happen, but it's pretty unlikely otherwise. The Infinite Monkey Theorem Simulator allows you to test this out for yourself, so why not give it a shot and see how your do?")

st.header('What will your monkeys "try" to type?')
st.subheader("Sonnet XVIII by William Shakespeare")
st.write(sonnet_xviii)
st.markdown("-------------------------")

st.header("Need some inspiration for your simulation? Here are some fun facts:")
st.markdown("- *It has been estimated that there are between 172,00 - 299,700 chimpanzees on Earth.*")
st.markdown("- *The average human types 40 words per minute, and 216 WPM is the world record.*")
st.markdown("- *In 2003, a computer was put inside an enclosure with six macaques. [Their finished product](https://web.archive.org/web/20130120215600/http://www.vivaria.net/experiments/notes/publication/NOTES_EN.pdf) was not exactly Shakespeare. They mostly typed the letter 's' before partially destroying the machine and using it as a toilet. [BBC.](http://news.bbc.co.uk/2/hi/3013959.stm)*")
st.markdown("- *Family Guy had an episode where Peter alludes to the infinite monkey theorem:*")
st.video('https://youtu.be/yv0j2MjZs0A',start_time=1)
st.markdown("- *But of course, The Simpsons did it first:*")
st.video('https://youtu.be/loMEF18Ir4s')
st.markdown("-------------------------")









