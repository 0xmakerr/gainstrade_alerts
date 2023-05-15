# gainstrade_alerts
My first ever Python project. Allowed me to learn the basics of Python coding and also learn web3.py, discord, http libraries, working with Docker and VPS providers.

Basic description of the project:

These python scripts helped me construct delta neutral funding trading strategies using the gains.trade decentralized trading platform.


funding.py - calculates the expected funding changes in a product, we input our desired collateral and leverage. In return we get how the funding rates will change in response to our trade.

fundingalerts.py - calculates all of the funding of all products on gains.trade and sends alerts to my discord server whenever there is a large funding opportunity present

positiontracker.py - enter my current positions on gains.trade platform and get alerts to discord if funding in these positions changes below a certain amount.
