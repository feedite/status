# Feedite Status
Automatically monitoring the status of Feedite

The application currently monitors the status of the following:
- Login Page
- Signup Page

### How does it work?
The application uses Python Selenium to first get screenshots of the pages being monitored. Next, it compares them to screenshots of working pages using Python ImageHash. It returns the result in the form of "OK" or "Not OK" through a Python Flask web app.

Results can also be publically viewed for debugging purposes.
