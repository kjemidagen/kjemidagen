package main

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

type Company struct {
	gorm.Model
	ID           string  `json:"id"`
	Title        string  `json:"title"`
	EmailAddress string  `json:"email_address"`
	Price        float64 `json:"price"`
	UserID 		 int 	 `json:"user_id"`
	User *User
}

func GetCompanies(c *gin.Context) {
	db := DBConn
	var companies []Company
	result := db.Find(&companys)
	fmt.Println(companies, result)
	c.JSON(http.StatusOK, companys)
}

func Getcompany(c *gin.Context) {
	id := c.Param("id")
	db := DBConn
	var company company
	db.First(&company, id)
	c.JSON(http.StatusOK, company)
}

func Postcompany(c *gin.Context) {
	db := DBConn
	var company company
	company.ID = 1
	company.companyame = "bucky"
	company.HashedPassword = "asndfjuiqanf"
	company.IsAdmin = true
	db.Create(&company)
	c.JSON(http.StatusCreated, company)
}

func Putcompany(c *gin.Context) {
	id := c.Param("id")
	db := DBConn
	var company company
	db.Find(&company, id)
	company.companyame = "bucky"
	company.HashedPassword = "asndfjuiqanf"
	company.IsAdmin = true
	db.Save(&company)
	c.JSON(http.StatusOK, company)
}

func Deletecompany(c *gin.Context) {
	id := c.Param("id")
	db := DBConn
	var company company
	db.First(&company, id)
	if company.companyame == "" {
		c.String(http.StatusInternalServerError, fmt.Sprintf("No book with id = %s!", id))
	}
	db.Delete(&company)
	c.String(http.StatusNoContent, "User deleted")
}
