#!/usr/bin/env python
# _*_ coding: utf-8 _*_
from Cms.Coremail import CoremailConfigurationFileLeakVulnerability
from ClassCongregation import Prompt
def Main(ThreadPool,Url,Values,UnixTimestamp):
    ThreadPool.Append(CoremailConfigurationFileLeakVulnerability.medusa, Url, Values, UnixTimestamp)
    Prompt("Coremail")