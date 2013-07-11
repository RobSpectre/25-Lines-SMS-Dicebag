# 25 Lines - SMS Dice Bag 

A Twilio application that serves as the Dungeon Master's SMS companion,
providing a text interface to random dice rolling.

[![Build
Status](https://secure.travis-ci.org/RobSpectre/25-Lines-SMS-Dicebag.png)]
(http://travis-ci.org/RobSpectre/25-Lines-SMS-Dicebag)


## Summary

A little stressed out one afternoon in the office, I decided to whip up another
Twilio 25-liner like the [SMS
Weather](https://github.com/RobSpectre/25-Lines-SMS-Weather) I put together earlier in the week.
Same rules applied here as the weather app, and I gave myself 50 total minutes
to complete:

* It had to do something significant.  Couldn't be something silly like
  [Laughotron](http://www.laughotron.com/).
* Start to finish in *no more* than 25 lines, including whitespace.
* It had to pass my [PEP8](http://www.python.org/dev/peps/pep-0008/) vim plugin.
  No crazy single-line, more than 80 column shenanigans.
* Application had to be code complete by the time [Super Marios Brothers alarm
  clock](http://www.cutesense.com/detail.php?pID=1545&title=Super-Mario-%26amp%3B--Yoshi-Stainless--Mini-Table-Alarm-Clock)
  went off.
* It must withstand a reasonable amount of poor user input - no brittleware.

To accomplish this, I busted out the [Twilio Hackpack for Heroku and
Flask](https://github.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask) and
my [second ed
DMG](http://www.amazon.com/Dungeon-Masters-Guide-Advanced-Dragons/dp/0880387297).

## Usage

Text anything to (646) 606-2920 to see it work!

![Example of it
working](https://raw.github.com/RobSpectre/25-Lines-SMS-Dicebag/master/images/usage.png)


## Installation

Step-by-step on how to deploy and develop this app.

### Deploy 

1) Grab latest source
<pre>
git clone git://github.com/RobSpectre/25-Lines-SMS-Dicebag.git 
</pre>

2) Install dependencies
<pre>
make init
</pre>

3) Navigate to folder and create new Heroku Cedar app
<pre>
heroku create --stack cedar
</pre>

4) Deploy to Heroku
<pre>
git push heroku master
</pre>

5) Scale your dynos
<pre>
heroku scale web=1
</pre>

6) Configure a new TwiML app and Twilio phone number to use the app.
<pre>
python configure.py --account_sid ACxxxxxx --auth_token yyyyyyy -n -N
</pre>

7) Text the new number and roll your next character!


### Development

Be sure to follow the configuration steps above and use this step-by-step guide to tweak to your heart's content.

1) Install the dependencies.
<pre>
make init
</pre>

2) Launch local development webserver
<pre>
foreman start
</pre>

3) Open browser to [http://localhost:5000](http://localhost:5000).

4) Tweak away on `app.py`.


## Testing

Damn straight this dice bag is tested.  We know how important those stat rolls
are.

<pre>
make test
</pre>



## Meta 

* No warranty expressed or implied.  Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by [Twilio New
 York](http://www.meetup.com/Twilio/New-York-NY/) 

[![githalytics.com
alpha](https://cruel-carlota.pagodabox.com/fa3df02d95a43ac0668ea3503d8baa82
"githalytics.com")](http://githalytics.com/RobSpectre/25-Lines-SMS-Dicebag)
