using Microsoft.EntityFrameworkCore;
using Kjemidagen.Models;
using Microsoft.Extensions.Configuration;


var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();
var server = builder.Configuration["DBServer"] ?? "localhost";
var port = builder.Configuration["DBPort"] ?? "5432";
var user = builder.Configuration["DBUser"] ?? "admin";
var password = builder.Configuration["DBPassword"] ?? "kjemidagen";
var database = builder.Configuration["Database"] ?? "kjemidagen";

builder.Services.AddDbContext<KjemidagenContext>(opt => 
    opt.UseNpgsql($"Host={server};Port={port};Username={user};Password={password};Database={database}"));

// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
    app.UseDeveloperExceptionPage();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

// Automatically migrates, don't think its very smart to do.
// using (var scope = app.Services.CreateScope())
//     {
//         var db = scope.ServiceProvider.GetRequiredService<KjemidagenContext>();
//         db.Database.Migrate();
//     }

app.Run();
