import logging
import os
from os import environ

from testcontainers.core.generic import DbContainer


class MariaDBContainer(DbContainer):

    def __init__(
        self,
        image="mysql:latest",
        logger: logging.Logger = None,
        MYSQL_USER=None,
        MYSQL_ROOT_PASSWORD=None,
        MYSQL_PASSWORD=None,
        MYSQL_DATABASE=None,
        **kwargs
    ):
        super(MariaDBContainer, self).__init__(image, **kwargs)
        self.port_to_expose = 3306
        self.__log = logger
        self.with_exposed_ports(self.port_to_expose)
        self.MYSQL_USER = MYSQL_USER or environ.get("MYSQL_USER", "test")
        self.MYSQL_ROOT_PASSWORD = MYSQL_ROOT_PASSWORD or environ.get(
            "MYSQL_ROOT_PASSWORD", "test"
        )
        self.MYSQL_PASSWORD = MYSQL_PASSWORD or environ.get("MYSQL_PASSWORD", "test")
        self.MYSQL_DATABASE = MYSQL_DATABASE or environ.get("MYSQL_DATABASE", "test")

        if self.MYSQL_USER == "root":
            self.MYSQL_ROOT_PASSWORD = self.MYSQL_PASSWORD

    def _configure(self):
        self.with_env("MYSQL_ROOT_PASSWORD", self.MYSQL_ROOT_PASSWORD)
        self.with_env("MYSQL_DATABASE", self.MYSQL_DATABASE)

        if self.MYSQL_USER != "root":
            self.with_env("MYSQL_USER", self.MYSQL_USER)
            self.with_env("MYSQL_PASSWORD", self.MYSQL_PASSWORD)

    def get_connection_url(self):
        url = super()._create_connection_url(
            dialect="mysql+pymysql",
            host=os.environ.get("TC_HOST"),
            username=self.MYSQL_USER,
            password=self.MYSQL_PASSWORD,
            db_name=self.MYSQL_DATABASE,
            port=self.port_to_expose,
        )
        self.__log.debug("Connection URL: %s", url)
        return url
