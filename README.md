# URL shortner service #
problem statement:
How Would You Design a URL Shortener Service Like TinyURL?
URL shortening services like bit.ly or TinyURL are very popular to generate shorter aliases for long URLs. 
You need to design this kind of web service where if a user gives a long URL then the service returns a short URL and if the user gives a short URL then it returns the original long URL.

For example, shortening the given URL through TinyURL:
https://www.abc_sample_webiste.com/how-to-code-better/practice-daily

output - http://bit.ly/[a-zA-z0-9] - (7 to 8 character). <br />

# HLD (High level design) #

front -> long_url, --> short with the help encoding --> check this is the unique short url -> database store. <br />
generating URL with the help of encoding technique.<br />
Storing the generated URL in database.

# Requirements Gathering #

Functional req
1. Creating a unique alias for the long url. <br />
2. short urls service should directly hit the original link. <br />
3. Link will expire after certain span of time <br />

Non functional req
1. Highly available system. If service is down redirection fails.
2. minimal latency.
3. shortened link should not be predictable.

# Data capacity (minimal latency) #
  Let’s assume our service has 20 M new URL shortenings per month. 
  Let’s assume we store every URL shortening request (and associated shortened link) for 5 years . <br /> 
 
  Calculation  = 20 Million * 5 years * 12 months = 1.2 B records <br />
 
  For this period the service will generate about 1.2 B records. <br />

  Consider the average long URL size of 2KB ie for 2048 characters. <br />
  Short URL size: 17 Bytes for 17 characters. <br />
  created_at- 7 bytes. <br />
  1 records will hold approx = 2.024 KB of data <br />

  As per the problem statement 20 M active user. Data capacity will be
  20000000 * 2.024 = 60780000 KB = 44.08 GB per month. <br />

encoding = [A-Z][a-z][0-9] = 26 + 26+ 10 = base 62. <br />

short_url of lenght 7 can generate = 62 ^7 = 3.5 trillion. <br />

Which can take more than 1000 years to exhaust completely considering the above load.

//you will check after creating every hash for collision and if the required short url is in db or not.

There is service which can manage our server and provide them partitioned and new range of counter to keep our hash collision free.
# Zookeeper #
Zookeeper will manage server providing new integer to create hash values.

server1 = 1 - 1 lac
server2 = 1 lac - 2 lacs
server3 = 2 lacs - 3 lacs

If a server goes down will be short on very low integers, But zookeeper service manages the add new server whenever old one is exhausted.
Also the new unused range is given to newly created server.

# Redis #

Once user will create it's short url. They will directly try to access the original link for confirmation. <br />
So using redis to cache the recently created url will be very useful and avoid db task.<br />
If did not find the the data inside cache. We can also implement elasticSearch. <br />
If we still not able to find the record then probably we can let db to give us the url. 

# Implementation #

Implementation of above application is done by using django. <br />
For database we are going to use rdbms. <br />
Frontend can be done in React or next.js .
