from typing import Any, Optional
from sqlalchemy.orm import Session
from app.schema.user_schema import UserSchemaBaseCreate, UserSchemaBaseUpdate
from app.models.base import CRUDBase
from app.models.user import UserModel


class UserCRUD(
        CRUDBase[UserModel, UserSchemaBaseCreate, UserSchemaBaseUpdate]
):

    def sync_get_by_openid(
        self, db: Session, openid: Any
    ) -> Optional[UserModel]:
        """
        同步方法
        根据表id获取对象
        """
        return db.query(self.model).filter(self.model.openid == openid).first()


user_crud = UserCRUD(UserModel)
