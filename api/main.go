package main

import (
	"fmt"
	"os"

	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

func setupRoutes(router *gin.Engine) {
	router.GET("/", func(c *gin.Context) {
		c.String(200, "Yep server works")
	})

	v1 := router.Group("/api/v1") 
	{
		v1.GET("/users", GetUsers)
		v1.GET("/users/:id", GetUser)
		v1.POST("/users", PostUser)
		v1.PUT("/users", PutUser)
		v1.DELETE("/users", DeleteUser)
	}
}

func initDatabase() {
	var err error
	host:=os.Getenv("DBServer")
	user := os.Getenv("DBUser")
	password := os.Getenv("DBPassword")
	//dbname := os.Getenv("Database")
	port := os.Getenv("DBPort")
	
	dsn := fmt.Sprintf("host=%s user=%s password=%s dbname=%s port=%s sslmode=disable", host, user, password, user, port)
	DBConn, err = gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		panic("Failed to connect to database provider")
	}
	fmt.Println("Database connection successfully opened")
}

func main() {
	godotenv.Load()
	router := gin.Default()
	initDatabase()
	setupRoutes(router)

	router.Run() // listen and serve on 0.0.0.0:8007 (for windows "localhost:8007"). Port is defined in .env
}