# hometap
# My Hometap Project



__*GitHub Repo*__:  Hometap  @  https://github.com/gregptm  

### ENV set up

<pre>
 git clone https://github.com/gregptm/hometap.git
 python3 -m venv hometap
 source hometap/bin/activate
 cd hometap
 pip install -r requirements.txt
</pre> 
 
### Run options by level of detail

<pre>
 pytest -v -s  testCases/test_zillowMortCalc.py               # all tests, verbose, with debug prints
 pytest -v  testCases/test_zillowMortCalc.py                  # all test verbose
 pytest -v -s -m L0 testCases/test_zillowMortCalc.py          # just L0 tests
 pytest -v -s -m L1 testCases/test_zillowMortCalc.py          # just Li test
 pytest testCases/test_zillowMortCalc.py                      # all tests - just pass or fail output
</pre>

### Issues:

<ul>
  <li>We assumed that the advanced feature did not yet exist in the cycle and we had just added interest rate to the base calculator. As such we cannot just shut off the PMI and TAXES without that UI, via front end automaton.</li>
    <ul>
      <li>Therefore a proxy is needed or defined IP or some such to get consistent taxes in the calculation of full monthly payment.  So as a temporary fix, knowing the Advanced feature is planned for a near future sprint, we currently are verifying monthly P&I added a TODO in code to add a proxy for this test when not also testing advanced.</li>
    </ul>  
  <li>Standardized custom ID’s are needed on all fields! Suggest ‘data-qa’.</li>
    <li>Weird form reaction to entering data. </li>
      <ul>
        <li>I had to use two clears and then a click to get a stable entry point that would clear and stick</li>
        <li>Even still, we need to have the last field entered not be the interest rate as it has a tendency to re assign itself a new value ?!?!</li>
      </ul>
    <li>Ran into API limits and added GH_TOKEN, but the it stopped working, ignoring the settings.</li>
      <ul>
        <li>So I tried running just FF driver direct vs the new manager way, and FF runs.</li>
        <li>However, I see that it fails to verify the new page test for the Current Rates link, added a TODO in code</li>
       <br>
        <li> NOTE : 5/31 - email arrived saying GitHub revoked the token. Reread the documentation and fixed the Token issue. FF still chokes on my verification of the Current Rates link - suspect a timing/window close issue.</li>
      </ul>
</ul>

### Observed:

The error message only appears for an error,  such that we need only to look for its existence in the case where we expect to find it,  else we get an <code>selenium.common.exceptions.NoSuchElementException</code>

