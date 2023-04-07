# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # Project Information
# MAGIC 
# MAGIC * Name: **Data Engineer Learning Path**
# MAGIC * Version:  **1.0.2**
# MAGIC * Built On: **Nov 4, 2022 at 22:07:03 UTC**

# COMMAND ----------

# MAGIC %md ## Trouble Shooting
# MAGIC The following section provides general information about troubleshooting courseware produced by Databricks Academy. Each section correlates to a specific error message that an end-user may receive with direct links to more advanced content.

# COMMAND ----------

# MAGIC %md ### Admin Required
# MAGIC 
# MAGIC Databricks Academy often requires the student to have admin privileges in a workspace to effect changes. In some cases, this is a byproduct of working through the courseware. However, in many cases, this is to configure the environment for users that would otherwise not require admin privileges.
# MAGIC 
# MAGIC For more current information, please <a href="https://files.training.databricks.com/static/troubleshooting.html#admin-required" target="_blank">Troubleshooting Admin Requirements</a>

# COMMAND ----------

# MAGIC %md ### Workspace Not Configured
# MAGIC 
# MAGIC Some of the content produced by Databricks Academy requires configuration (or re-configuration) of the workspace and its assets. This configuration includes complete tasks like creating cluster policies, cluster pools, granting specific user permissions, and other such tasks.
# MAGIC 
# MAGIC This error generally indicates that the notebook [Workspace-Setup]($./Includes/Workspace-Setup) was not executed.
# MAGIC 
# MAGIC For more current information, please <a href="https://files.training.databricks.com/static/troubleshooting.html#workspace-setup" target="_blank">Troubleshooting Workspace Setup</a>

# COMMAND ----------

# MAGIC %md ### Spark Version
# MAGIC 
# MAGIC To ensure that all labs execute as expected, Databricks Academy requires that the content provided be executed against a cluster configured with a specific runtime. Typically this is an LTS (long-term supported) version.
# MAGIC 
# MAGIC This course is tested against and requires one of the following DBRs (Databricks Runtime): **11.3.x-scala2.12, 11.3.x-photon-scala2.12, 11.3.x-cpu-ml-scala2.12**.
# MAGIC 
# MAGIC For more current information, please <a href="https://files.training.databricks.com/static/troubleshooting.html#spark-version" target="_blank">Troubleshooting the Spark Version</a>

# COMMAND ----------

# MAGIC %md ### Cannot write to DBFS
# MAGIC 
# MAGIC DBFS stands for Databricks File System and is a virtual file system that Databricks Academy uses to read data from and write data to. There are two primary locations, and depending on the courseware, some tertiary locations.
# MAGIC  
# MAGIC The first location is **dbfs:/mnt/dbacademy-datasets/**, which is a storage location for datasets used by this course. Datasets are downloaded from our data repositories and copied to this location to provide faster, in-region access to the course's datasets. Files written to this location are expected to be treated as read-only and shared by all consumers of this courseware.
# MAGIC 
# MAGIC The second location is **dbfs:/mnt/dbacademy-users/**, a storage location for user-specific datasets and misc files generated by working through the courseware. This folder is subdivided by user and then by course, creating a per-user-per-course working directory.
# MAGIC 
# MAGIC In some cases, tertiary data may be written to **dbfs:/user/** as a default storage location for Spark and Spark tables. Like dbacademy-users, this folder is subdivided by user.
# MAGIC 
# MAGIC For more current information, please <a href="https://files.training.databricks.com/static/troubleshooting.html#cannot-write-dbfs" target="_blank">Troubleshooting DBFS Writes</a>

# COMMAND ----------

# MAGIC %md ### Cannot Install Libraries
# MAGIC 
# MAGIC Databricks Academy provides custom libraries to facilitate the development of its courseware. Your cluster requires access to these remotely hosted libraries so that they can be installed into your cluster.
# MAGIC 
# MAGIC Various companies restrict access to external sites to limit data exfiltration and address other security concerns, such as leaking potentially sensitive or proprietary information.
# MAGIC 
# MAGIC For more current information, please see <a href="https://files.training.databricks.com/static/troubleshooting.html#cannot-install-libraries" target="_blank">Troubleshooting Library Installation</a>

# COMMAND ----------

# MAGIC %md ### Requires Unity Catalog
# MAGIC 
# MAGIC Unity Catalog (UC) is a service provided by Databricks. This courseware requires that the workspace be UC Enabled. However, not all workspaces have (or can have) this feature enabled.
# MAGIC 
# MAGIC For more current information, please see <a href="https://files.training.databricks.com/static/troubleshooting.html#requires-unity-catalog" target="_blank">Troubleshooting Unity Catalog Requirements</a>

# COMMAND ----------

# MAGIC %md ### Cannot Create Schema
# MAGIC 
# MAGIC This course will require you to create a schema (aka database) which in turn requires that you have the necessary permissions. Sometimes, this is done as part of building a more complex example. But in most cases, the schema being created is a user-specific schema used to provide user-level isolation as multiple students work through various lessons in the same workspace.
# MAGIC 
# MAGIC For more current information, please see <a href="https://files.training.databricks.com/static/troubleshooting.html#cannot-create-schema" target="_blank">Troubleshooting Creating Schemas</a>

# COMMAND ----------

# MAGIC %md ### Cannot Create Catalog
# MAGIC 
# MAGIC This course will require you to create a catalog (typically in conjunction with using Unity Catalog) which in turn requires that you have the necessary permissions. In most cases, the new catalog is a user-specific catalog used to provide user-level isolation as multiple students work through various lessons in the same workspace.
# MAGIC 
# MAGIC For more current information, please see <a href="https://files.training.databricks.com/static/troubleshooting.html#cannot-create-catalog" target="_blank">Troubleshooting Creating Catalogs</a>

# COMMAND ----------

# MAGIC %md ## Copyrights
# MAGIC This section documents the various copyrights as they relate to the datasets used in this course.
# MAGIC 
# MAGIC Run the following cell for additional information on this course's datasets, and their copyrights.

# COMMAND ----------

# MAGIC %run ./Includes/Print-Dataset-Copyrights

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
