# Postmortem

<div style="display:flex;justify-content:center;">
    <a href="https://twitter.com/devopsreact/status/834887829486399488" target="_blank"><img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/294/pQ9YzVY.gif" alt="" loading="lazy" style="">
    </a>
</div>

<br>

### Summary
On the 2nd of June 2024, between 10:00 AM - 12:00 PM CAT, 100% of our users were unable to access our Scholarly app due to database misconfiguration during maintenance

## Timeline

10:00 AM CAT - Routine database maintenance was initiated to upgrade the database version. Users began experiencing connectivity issues and were unable to access the app

10:15 AM CAT - Monitoring systems alerted the engineering team about high error rates and user reports of the app unavailability began to surface

10:30 AM CAT - It was identified that the database configuration changes made during maintenance caused the database to reject connections from the application server. Engineers attempted to rollback the database configuration changes

11:00 AM CAT - The rollback process was initiated, but the app remained unavailable due to residual configuration errors. A deeper investigation revealed additional configuration files that needed correction

11:30 AM CAT - All configuration files were corrected and verified. The database connections were successfully restored.  The app was tested for stability and accessibility

12:00 PM CAT - The app was fully restored to normal operation. Users regained full access

## Root Cause Analysis

The root cause of the outage was a misconfiguration in the database settings during routine upgrade. The specific configuration that caused the problem was the incorrect setting of the `db_connection_limit` parameter, which was set to a value that was too low to handle the usual load from the app

## Resolution and Recovery

1. Rollback Configuration: The database configuration changes were rolled back to the previous stable state.
2. Verification: All related configuration files were checked and corrected to ensure proper settings.
3. Testing: The app was rigorously tested before fully restoring services to the users.

## Corrective Actions

To prevent similar incidents in the future, the following actions will be taken:

1. Pre-deployment Testing: Implement a more robust pre-deployment testing process to catch configuration issues before they affect production.
2. Configuration Review: Establish a peer review system for all configuration changes.
3. Automated Monitoring: Enhance monitoring tools to detect and alert on potential configuration issues immediately.
4. Incident Response Training: Conduct regular incident response drills to ensure the engineering team is well-prepared for future incidents.

## Lessons Learned

1. Importance of Pre-deployment Testing: Ensuring all changes are thoroughly tested can prevent production issues.
2. Configuration Management: Maintaining strict control and review of configuration changes is crucial.
3. Effective Communication: Prompt communication with users about ongoing issues can help manage user expectations and reduce frustration.

## Conclusion

This incident highlighted areas for improvement in our deployment and monitoring processes. By taking the corrective actions outlined above, we aim to reduce the likelihood of similar incidents in the future and improve our overall system reliability.