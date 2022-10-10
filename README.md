# Feedite Status
Automatically monitoring the status of Feedite

The application currently monitors the statuses of the following:
- Login Page
- Signup Page

### How does it work?
The application uses Python Selenium to first get screenshots of the pages being monitored. Next, it compares them to screenshots of working pages using Python ImageHash.
