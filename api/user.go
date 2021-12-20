package main

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	ID             int `json:"id"`
	Userame        string `json:"username"`
	HashedPassword string `json:"hashed_password"`
	IsAdmin        bool   `json:"is_admin"`
	Company *Company 
}

func GetUsers(c *gin.Context) {
	db := DBConn
	var users []User
	result := db.Find(&users)
	fmt.Println(users, result)
	c.JSON(http.StatusOK, users)
}

func GetUser(c *gin.Context) {
	id := c.Param("id")
	db := DBConn
	var user User
	db.First(&user, id)
	c.JSON(http.StatusOK, user)
}

func PostUser(c *gin.Context) {
	db := DBConn
	var user User
	user.ID = 1
	user.Userame = "bucky"
	user.HashedPassword = "asndfjuiqanf"
	user.IsAdmin = true
	db.Create(&user)
	c.JSON(http.StatusCreated, user)
}

func PutUser(c *gin.Context) {
	id := c.Param("id")
	db := DBConn
	var user User
	db.Find(&user, id)
	user.Userame = "bucky"
	user.HashedPassword = "asndfjuiqanf"
	user.IsAdmin = true
	db.Save(&user)
	c.JSON(http.StatusOK, user)
}

func DeleteUser(c *gin.Context) {
	id := c.Param("id")
	db := DBConn
	var user User
	db.First(&user, id)
	if user.Userame == "" {
		c.String(http.StatusInternalServerError, fmt.Sprintf("No book with id = %s!", id))
	}
	db.Delete(&user)
	c.String(http.StatusNoContent, "User deleted")
}