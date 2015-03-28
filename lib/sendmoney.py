import random
from Crypto.PublicKey import RSA
from mastercard_api_python.common import environment
from mastercard_api_python.tests import testutils
from mastercard_api_python.services.moneysend.services import transferservice
from mastercard_api_python.services.moneysend.domain.transfer import transferrequest
from mastercard_api_python.services.moneysend.domain.transfer import paymentrequest
from mastercard_api_python.services.moneysend.domain.transfer import senderaddress
from mastercard_api_python.services.moneysend.domain.transfer import fundingcard
from mastercard_api_python.services.moneysend.domain.transfer import receiveraddress
from mastercard_api_python.services.moneysend.domain.transfer import receivingamount
from mastercard_api_python.services.moneysend.domain.transfer import cardacceptor
from mastercard_api_python.services.moneysend.domain.transfer import fundingmapped
from mastercard_api_python.services.moneysend.domain.transfer import fundingamount
from mastercard_api_python.services.moneysend.domain.transfer import receivingmapped
from mastercard_api_python.services.moneysend.domain.transfer import receivingcard

SANDBOX_CONSUMER_KEY = \
        '7kIcg1Vq_-7tDlH3w4V671sRM5__MfW0qO42pOm3f31833d4!434c6c6966474877636d6848416b417662364b7a4f773d3d'
SANDBOX_PRIVATE_KEY_PATH = 'RaymondJacobson.key'
SANDBOX_PRIVATE_KEY_PASSWORD = '' # no password applied

class CryptoUtils():
    def __init__(self, environment):
        self._environment = environment

    def get_private_key(self):
        if self._environment == "PRODUCTION":
            return RSA.importKey(open(PRODUCTION_PRIVATE_KEY_PATH, 'r').read(),
                                      PRODUCTION_PRIVATE_KEY_PASSWORD)
        else:
            return RSA.importKey(open(SANDBOX_PRIVATE_KEY_PATH, 'r').read(),
                                      SANDBOX_PRIVATE_KEY_PASSWORD)

class SendMoney():
  def __init__(self):
    c_utils = CryptoUtils(environment.Environment.SANDBOX)
    _service = transferservice.TransferService(SANDBOX_CONSUMER_KEY,
                                               c_utils.get_private_key(),
                                               environment.Environment.SANDBOX)
  def transfer_request(self):
    print "yeah, bitch!"
