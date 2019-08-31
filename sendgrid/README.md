# Sendgrid


### Getting Started

Create a new sendgrid function:

```bash
# Create a new function from the sendgrid template
hof function create sendgrid "#sendgrid"

# Move into new function folder
cd sendgrid
```

Create the secret for your API key.

```bash
# Put your API key into a file
echo "<SENDGRID_APIKEY>" > secrets/apikey.env

# Create your secret in Hofstadter Studios
hof secrets create sendgrid-secret secrets/apikey.env
```

TODO:

Edit the configuration and content...

Push the function...

Call the function...

Integrate with a Studios app...

### References

https://github.com/sendgrid/sendgrid-python/

https://github.com/sendgrid/sendgrid-python/blob/master/examples/helpers/mail_example.py
