from django.db import models
from core import models as core_models
import jsonfield
import time

# Create your models here.
"""
Tables :
    
    2. FLProject    ==>     store model architecture and model weight
    
"""


class FLProject(models.Model):

    """
    with this table we will build new FL project and store it's information .

    column :

        1. project unique id
        2. project name
        3. project title
        4. model architecture json file
        5. model weight json file

    relation :

        1. user (every user can create project )      ==> foreign key
        2. user (every user can join this project)    ==> many to many

    """

    # unique id for identify project
    unique_id = models.CharField(max_length=250)

    # project name
    name = models.CharField(max_length=30)

    # project title
    title = models.TextField(max_length=30)

    # model architecture
    model_arch = jsonfield.JSONField(default={})

    # model weight
    weight = jsonfield.JSONField(default={})

    # relation
    project_owner = models.ForeignKey(core_models.ResearcherUser, on_delete=models.CASCADE)
    project_node_user = models.ManyToManyField(core_models.ResearcherUser, null=True)

    def __str__(self):
        return str(self.unique_id)


class ProjectRequest(models.ForeignKey):

    """
    with this table we will build user's request to join project

    column :

        1. unique id
        2. response status
        3. request time
        4. response time

    relation :

        1. FLProject    ==> foreign key

    """

    # unique id
    unique_id = models.CharField(max_length=25)

    # response status for determine project owner accept this request
    # or reject request
    # if project owner didn't answer it will ignore status
    request_status_tuple = (

        ('A', 'Accept'),
        ('I', 'Ignor'),
        ('R', 'Reject'),

    )
    response_status = models.CharField(max_length=1, choices=request_status_tuple, default='I')

    # store request time
    request_time = models.FloatField(default=time.time())

    # response time
    response_time = models.FloatField(null=True)

    # relation
    project = models.ForeignKey(FLProject, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.unique_id)


class TrainHist(models.Model):

    """
    with this table we will store every node's training history

    column :

        1. unique id
        2. avg loss     ==> this param store training average loss
        3. loss list    ==> this param store epoch's loss list
        4. final loss   ==> this param store final epoch loss
        5. avg acc      ==> this param store training average accuracy
        6. acc list     ==> this param store epoch's accuracy list
        7. final acc    ==> this param store final accuracy
        8. epoch num    ==> this param store number of epoch
    """