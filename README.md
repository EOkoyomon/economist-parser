# economist-parser
Extracts basics html elements (minimal styling) from economist articles that you have "reached your article limit" on.

Sorry, this script was a 30-60 minute procrastination so not fully fledged. Urllib requests pull different html page content than browsers so my initial intention of just providing a url did not work. Super naive and not really robust/scalable to structural changes on the website (such as renaming). Let me know if it no longer works.

# To Use:
1. On Chrome, visit an economist page with this "You've reached your article limit", such as https://www.economist.com/blogs/buttonwood/2014/03/demography-and-inequality
2. Right-click the page and hit View Page Source.
3. Save the page source (Ctrl-S or Cmd-S for example) and save the file, for example, under downloads.
4. Run the script as follows, providing the absolute path to your file (or relative from where the script lives if you know this):
    python3 Economist.py <absolute_path> <output_name>
5. The output(s) will be located at output_name#.txt where # is an integer. Should only be 1 but I loop just in case.

Example:
  With the URL provided above downloaded and saved in econ.html and my script living in Desktop (same directory as Downloads):
  python3 Economist.py ../Downloads/econ.html economist
  
  Outputs economist1.html in Desktop that can now be opened in a browser:
  
  ![Alt text](/screenshot.png?raw=true "Optional Title")

** Note screenshot does not say economist1 - I created the path displayed in the browser
