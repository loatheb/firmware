from ..i18n import gettext as _, keys as i18n_keys
from .common import FullSizeWindow, lv
from .components.container import ContainerFlexCol
from .components.listitem import DisplayItem
from .components.qrcode import QRCode


class Address(FullSizeWindow):
    def __init__(self, title, path, address, xpubs=None, multisig_index=0):
        super().__init__(title, None, confirm_text=_(i18n_keys.BUTTON__DONE))
        self.qr = QRCode(self, address)
        self.qr.align_to(self.title, lv.ALIGN.OUT_BOTTOM_MID, 0, 48)
        self.container = ContainerFlexCol(self, self.qr)
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__PATH__COLON), path
        )
        self.item2 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__ADDRESS__COLON), address
        )
        if xpubs:
            self.title.align(lv.ALIGN.TOP_MID, 0, 100)
            self.btn_yes.align(lv.ALIGN.BOTTOM_MID, 0, -30)
        for i, xpub in enumerate(xpubs or []):
            self.item3 = DisplayItem(
                self.container,
                _(i18n_keys.LIST_KEY__XPUB_STR_MINE__COLON).format(i + 1)
                if i == multisig_index
                else _(i18n_keys.LIST_KEY__XPUB_STR_COSIGNER__COLON).format(i + 1),
                xpub,
            )
        self.container.set_style_max_height(150, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.container.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


class XpubOrPub(FullSizeWindow):
    def __init__(self, title, path, xpub=None, pubkey=None):
        super().__init__(
            title, None, _(i18n_keys.BUTTON__EXPORT), _(i18n_keys.BUTTON__CANCEL)
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__PATH__COLON), path
        )
        self.item2 = DisplayItem(
            self.container,
            _(i18n_keys.LIST_KEY__XPUB__COLON)
            if xpub
            else _(i18n_keys.LIST_KEY__PUBLIC_KEY__COLON),
            xpub or pubkey,
        )


class Message(FullSizeWindow):
    def __init__(self, title, address, message):
        super().__init__(
            title, None, _(i18n_keys.BUTTON__SIGN), _(i18n_keys.BUTTON__CANCEL)
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__ADDRESS__COLON), address
        )
        self.item2 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__MESSAGE__COLON), message
        )
        self.item2.set_style_max_height(300, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.item2.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


class TransactionOverview(FullSizeWindow):
    def __init__(self, title, amount, address):
        super().__init__(
            title, None, _(i18n_keys.BUTTON__CONTINUE), _(i18n_keys.BUTTON__CANCEL)
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container,
            f"{_(i18n_keys.INSERT__SEND)} #ffffff {amount} # {_(i18n_keys.INSERT__TO)}:",
            address,
        )
        self.item1.label_top.set_recolor(True)


class TransactionDetailsETH(FullSizeWindow):
    def __init__(
        self,
        title,
        address_from,
        address_to,
        amount,
        fee_max,
        is_eip1559=False,
        gas_price=None,
        max_priority_fee_per_gas=None,
        max_fee_per_gas=None,
        total_amount=None,
    ):
        super().__init__(
            title,
            None,
            _(i18n_keys.BUTTON__HOLD_TO_SIGN),
            _(i18n_keys.BUTTON__REJECT),
            hold_confirm=True,
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__AMOUNT__COLON), amount
        )
        if not is_eip1559:
            self.item2 = DisplayItem(
                self.container, _(i18n_keys.LIST_KEY__GAS_PRICE__COLON), gas_price
            )
        else:
            self.item2 = DisplayItem(
                self.container,
                _(i18n_keys.LIST_KEY__PRIORITY_FEE_PER_GAS__COLON),
                max_priority_fee_per_gas,
            )
            self.item2_1 = DisplayItem(
                self.container,
                _(i18n_keys.LIST_KEY__MAXIMUM_FEE_PER_GAS__COLON),
                max_fee_per_gas,
            )
        self.item3 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__MAXIMUM_FEE__COLON), fee_max
        )
        self.item4 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__TO__COLON), address_to
        )
        self.item5 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__FROM__COLON), address_from
        )
        if total_amount is None:
            total_amount = f"{amount}\n{fee_max}"
        self.item6 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__TOTAL_AMOUNT__COLON), total_amount
        )
        self.container.set_style_max_height(350, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.container.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


class ContractDataOverview(FullSizeWindow):
    def __init__(self, title, description, data):
        super().__init__(
            title, None, _(i18n_keys.BUTTON__CONTINUE), _(i18n_keys.BUTTON__CANCEL)
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__SIZE__COLON), description
        )
        self.item2 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__DATA__COLON), data
        )
        self.item2.set_style_max_height(300, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.item2.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


class BlobDisPlay(FullSizeWindow):
    def __init__(
        self,
        title,
        description: str,
        content: str,
        icon_path: str = "A:/res/shriek.png",
    ):
        super().__init__(
            title,
            None,
            _(i18n_keys.BUTTON__CONTINUE),
            _(i18n_keys.BUTTON__CANCEL),
            icon_path=icon_path,
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(self.container, description, content)
        self.item1.set_style_max_height(400, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.item1.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


class ConfirmMetaData(FullSizeWindow):
    def __init__(self, title, subtitle, description, data):
        super().__init__(
            title, subtitle, _(i18n_keys.BUTTON__CONTINUE), _(i18n_keys.BUTTON__CANCEL)
        )
        if description:
            self.container = ContainerFlexCol(self, self.subtitle, pos=(0, 48))
            self.item1 = DisplayItem(self.container, description + ":", data)
            self.item1.set_style_max_height(400, lv.PART.MAIN | lv.STATE.DEFAULT)
            self.item1.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


class TransactionDetailsBTC(FullSizeWindow):
    def __init__(self, title: str, amount: str, fee: str, total: str):
        super().__init__(
            title,
            None,
            _(i18n_keys.BUTTON__HOLD_TO_SIGN),
            _(i18n_keys.BUTTON__REJECT),
            hold_confirm=True,
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__AMOUNT__COLON), amount
        )
        self.item2 = DisplayItem(self.container, _(i18n_keys.LIST_KEY__FEE__COLON), fee)
        self.item3 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__TOTAL_AMOUNT__COLON), total
        )
        self.container.set_style_max_height(350, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.container.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


class JointTransactionDetailsBTC(FullSizeWindow):
    def __init__(self, title: str, amount: str, total: str):
        super().__init__(
            title,
            None,
            _(i18n_keys.BUTTON__HOLD_TO_SIGN),
            _(i18n_keys.BUTTON__REJECT),
            hold_confirm=True,
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__AMOUNT_YOU_SPEND__COLON), amount
        )
        self.item3 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__TOTAL_AMOUNT__COLON), total
        )
        self.container.set_style_max_height(350, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.container.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


class ModifyFee(FullSizeWindow):
    def __init__(self, description: str, fee_change: str, fee_new: str):
        super().__init__(
            _(i18n_keys.TITLE__MODIFY_FEE),
            None,
            _(i18n_keys.BUTTON__CONTINUE),
            _(i18n_keys.BUTTON__CANCEL),
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(self.container, description, fee_change)
        self.item2 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__NEW_FEE__COLON), fee_new
        )


class ModifyOutput(FullSizeWindow):
    def __init__(
        self, address: str, description: str, amount_change: str, amount_new: str
    ):
        super().__init__(
            _(i18n_keys.TITLE__MODIFY_AMOUNT),
            None,
            _(i18n_keys.BUTTON__CONTINUE),
            _(i18n_keys.BUTTON__CANCEL),
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__ADDRESS__COLON), address
        )
        self.item2 = DisplayItem(self.container, description, amount_change)
        self.item3 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__NEW_AMOUNT__COLON), amount_new
        )


class ConfirmReplacement(FullSizeWindow):
    def __init__(self, title: str, txid: str):
        super().__init__(
            title, None, _(i18n_keys.BUTTON__CONTINUE), _(i18n_keys.BUTTON__CANCEL)
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__TRANSACTION_ID__COLON), txid
        )
        # self.item1.set_style_max_height(400, lv.PART.MAIN | lv.STATE.DEFAULT)
        # self.item1.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


class ConfirmPaymentRequest(FullSizeWindow):
    def __init__(self, title: str, subtitle, amount: str, to_addr: str):
        super().__init__(
            title,
            subtitle,
            _(i18n_keys.BUTTON__HOLD_TO_SIGN),
            _(i18n_keys.BUTTON__REJECT),
            hold_confirm=True,
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__TO__COLON), to_addr
        )
        self.item2 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__AMOUNT__COLON), amount
        )
        self.container.set_style_max_height(350, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.container.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


class ConfirmDecredSstxSubmission(FullSizeWindow):
    def __init__(self, title: str, subtitle: str, amount: str, to_addr: str):
        super().__init__(
            title, subtitle, _(i18n_keys.BUTTON__CONTINUE), _(i18n_keys.BUTTON__CANCEL)
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__AMOUNT__COLON), amount
        )
        self.item2 = DisplayItem(
            self.container, -(i18n_keys.LIST_KEY__TO__COLON), to_addr
        )


class ConfirmCoinJoin(FullSizeWindow):
    def __init__(
        self, title: str, coin_name: str, max_rounds: str, max_fee_per_vbyte: str
    ):
        super().__init__(
            title, None, _(i18n_keys.BUTTON__CONTINUE), _(i18n_keys.BUTTON__CANCEL)
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__COIN_NAME__COLON), coin_name
        )
        self.item2 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__MAXIMUM_ROUNDS__COLON), max_rounds
        )
        self.item3 = DisplayItem(
            self.container,
            _(i18n_keys.LIST_KEY__MAXIMUM_MINING_FEE__COLON),
            max_fee_per_vbyte,
        )


class ConfirmSignIdentity(FullSizeWindow):
    def __init__(self, title: str, identity: str, subtitle: str | None):
        super().__init__(
            title, subtitle, _(i18n_keys.BUTTON__CONTINUE), _(i18n_keys.BUTTON__CANCEL)
        )
        align_base = self.title if subtitle is None else self.subtitle
        self.container = ContainerFlexCol(self, align_base, pos=(0, 48))
        self.item1 = DisplayItem(
            self.container, _(i18n_keys.LIST_KEY__IDENTITY__COLON), identity
        )


class ConfirmProperties(FullSizeWindow):
    def __init__(self, title: str, properties: list[tuple[str, str]]):
        super().__init__(
            title, None, _(i18n_keys.BUTTON__CONTINUE), _(i18n_keys.BUTTON__CANCEL)
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        for key, value in properties:
            self.item = DisplayItem(self.container, f"{key.upper()}", value)
        self.container.set_style_max_height(400, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.container.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)


class ConfirmTransferBinance(FullSizeWindow):
    def __init__(self, items: list[tuple[str, str, str]]):
        super().__init__(
            _(i18n_keys.TITLE__CONFIRM_TRANSFER),
            None,
            _(i18n_keys.BUTTON__HOLD_TO_SIGN),
            _(i18n_keys.BUTTON__REJECT),
            hold_confirm=True,
        )
        self.container = ContainerFlexCol(self, self.title, pos=(0, 48))
        for key, value, address in items:
            self.item1 = DisplayItem(self.container, key, "")
            self.item2 = DisplayItem(
                self.container, _(i18n_keys.LIST_KEY__AMOUNT__COLON), value
            )
            self.item3 = DisplayItem(
                self.container, _(i18n_keys.LIST_KEY__TO__COLON), address
            )
        self.container.set_style_max_height(350, lv.PART.MAIN | lv.STATE.DEFAULT)
        self.container.set_scrollbar_mode(lv.SCROLLBAR_MODE.AUTO)
