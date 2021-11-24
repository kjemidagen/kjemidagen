# #See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["Kjemidagen.csproj", "mappe/"]
RUN dotnet restore "mappe/Kjemidagen.csproj"
COPY . ./mappe
WORKDIR "/src/mappe"
RUN dotnet build "Kjemidagen.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Kjemidagen.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Kjemidagen.dll", "--environment==Development"]

# # https://hub.docker.com/_/microsoft-dotnet
# FROM mcr.microsoft.com/dotnet/sdk:6.0
# WORKDIR /app
# COPY . .
# RUN dotnet restore
# RUN dotnet dev-certs https
# ENTRYPOINT ["dotnet", "watch", "run"]