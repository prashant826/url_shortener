# # ------------------------------------  URL shortner service -----------------------------
# problem statement:
# How Would You Design a URL Shortener Service Like TinyURL?
# URL shortening services like bit.ly or TinyURL are very popular to generate shorter aliases for long URLs. 
# You need to design this kind of web service where if a user gives a long URL then the service returns a short URL and if the user gives a short URL then it returns the original long URL.

# For example, shortening the given URL through TinyURL:
# https://www.abc_sample_webiste.com/how-to-code-better/practice-daily

# output - http://bit.ly/3uQqImU


front -> long_url, --> short with the help encoding --> check this is the unique short url -> database store(url span) -> user

# # -------------------------------------- HLD (High level design) -------------------------
# generating URL with the help of encoding technique.
# Storing the generated URL in database.

# # ------------------------------------- Requirements Gathering ---------------------------

# Functional req
# 1. Creating a unique alias for the long url.
# 2. short urls service should directly hit the original link.
# 3. Link will expire after certain span of time

# Non functional req
# 1. Highly available system. If service is down redirection fails.
# 2. minimal latency.
# 3. shortened link should not be predictable.

# # ------------------------------------- Data capacity (minimal latency) -------------------
#  Let’s assume our service has 20 M new URL shortenings per month. 
#  Let’s assume we store every URL shortening request (and associated shortened link) for 5 years . 
 
#  Calculation  = 20 Million * 5 years * 12 months = 1.2 B records
 
#  For this period the service will generate about 1.2 B records.


# -----------------------------  Zookeepeer service -----------------------------------------

encoding = [A-Z][a-z][0-9] = 26 + 26+ 10 = base 62

short_url of lenght 7 can generate = 62 ^7 = 3.5 trillion.

Which can take more than 1000 years to exhaust completely considering the above load.

//you will check after creating every hash for collision and if the required short url is in db or not.

There is service which can manage our server and provide them partitioned and new range of counter to keep our hash collision free.
## Zookeeper ##
Zookeeper will manage server providing new integer to create hash values.

server1 = 1 - 1 lac
server2 = 1 lac - 2 lacs
server3 = 2 lacs - 3 lacs

If a server goes down will be short on very low integers, But zookeeper service manages the add new server whenever old one is exhausted.
Also the new unused range is given to newly created server.

# ----------------------------- Redis -------------------------------------------------

## Redis ##

Once user will create it's short url. They will directly try to access the original link for confirmation.
So using redis to cache the recently created url will be very useful and avoid db task.
If did not find the the data inside cache. We can also implement elasticSearch.
If we still not able to find the record then probably we can let db to give us the url. 



## ------------------------------------------ Implementation -------------------------------------

Implementation of above application is done by using django.
