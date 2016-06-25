PyGre.io
========

I'm proposing Python courses for free (as in beer), free (as in speech) and open to all,
in Grenoble, France. This repository holds the code of the website allowing people
to subscribe to the courses, and will be used as a use case during the course.

Tell me more !
--------------

The website is based on Tornado, and uses MongoDB for the users & calendar database.

The only personal data required to register for a course is an email address,
which will be used to send course updates to the students. First and last names
are optional, and any data sent through the website will be used strictly for
this purpose only (I don't do this for money and don't intend to sell your private
information to anyone).

The website specifications are as following:
- It displays a home page explaining briefly what PyGre is about.
- It shows the list of courses available to register for in the future, with details on date/time, location, the program of the course, and how many people have registered so far.
- A form to register to a course, that only requires an email address (names & other details are optional).
- In the future, a comment system where people who registered and attended a course can leave anonymous remarks and feedback.

A login system would be interesting, to quickly register to courses, to see
the agenda of courses one has registered to, to leave comments etc..

Why is everything in English ?
------------------------------

Like most programming languages, Python's syntax is based on English.
The website will eventually be internationalised. If you see a bad translation or want to contribute
to adding other languages, I'm gladly accepting pull requests.

License
-------

**The MIT License (MIT)** - Copyright © 2016 François Best

Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction,
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE
AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
