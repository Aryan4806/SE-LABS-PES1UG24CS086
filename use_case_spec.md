**Use Case ID:** UC-001  
**Use Case Name:** Monitor Microservice Health & Alert  
**Primary Actor:** DevOps Engineer  

---

* **Preconditions:**  
  1. Microservice health check URL is registered in the catalog.  
  2. Notification channels (e.g., Slack Webhook) are configured.  

* **Postconditions:**  
  1. Service health metrics are updated in the rolling 24-hour availability database.  
  2. Failure logs and alert messages are dispatched if failure thresholds are met.
1. System automated pinger sends HTTP GET health request to target microservice at 30-second intervals.
2. Target microservice returns `200 OK` HTTP status code within expected timeout window.
3. System logs successful health check metric.
4. System updates rolling 24-hour availability percentage display on dashboard.
* **At Step 2 of MSS:** Target microservice fails to respond or returns non-200 HTTP code.
  * **2a1.** System flags probe attempt as failed and increments failure counter.
  * **2a2.** System re-probes service immediately.
  * **2a3.** If 3 consecutive probes fail, system updates microservice status to `CRITICAL/DOWN`.
  * **2a4.** System triggers automated alert rule (*includes <<extend>> UC-002: Dispatch Incident Notification*).
  * **2a5.** System logs downtime event timestamp and resumes background pinging routine.
