from eth_keys.datatypes import PrivateKey
from eth_typing import Address

from eth.vm.forks.berlin.transactions import (
    BerlinTransactionBuilder,
    BerlinUnsignedLegacyTransaction,
    BerlinLegacyTransaction,
)

from eth._utils.transactions import (
    create_transaction_signature,
)

class SimpleLegacyTransaction(BerlinLegacyTransaction):
    pass


class SimpleUnsignedLegacyTransaction(BerlinUnsignedLegacyTransaction):
    def as_signed_transaction(self,
                              private_key: PrivateKey,
                              chain_id: int = None) -> BerlinLegacyTransaction:
        v, r, s = create_transaction_signature(self, private_key, chain_id=chain_id)
        return SimpleLegacyTransaction(
            nonce=self.nonce,
            gas_price=self.gas_price,
            gas=self.gas,
            to=self.to,
            value=self.value,
            data=self.data,
            v=v,
            r=r,
            s=s,
        )

class SimpleTransactionBuilder(BerlinTransactionBuilder):
    legacy_signed = SimpleLegacyTransaction
    legacy_unsigned = SimpleUnsignedLegacyTransaction

'''
class SimpleUnsignedTransaction(BerlinUnsignedTransaction):
    def as_signed_transaction(self,
                              private_key: PrivateKey,
                              chain_id: int = None) -> SimpleTransaction:
        v, r, s = create_transaction_signature(self, private_key, chain_id=chain_id)
        return SimpleTransaction(
            nonce=self.nonce,
            gas_price=self.gas_price,
            gas=self.gas,
            to=self.to,
            value=self.value,
            data=self.data,
            v=v,
            r=r,
            s=s,
        )
'''