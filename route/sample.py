from flask import Blueprint, request, json
from controller.sampleController import sampleController

sample = Blueprint('sample', __name__)
sample.route('', methods=['GET'])(sampleController.get_data)
