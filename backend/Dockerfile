#See https://aka.ms/containerfastmode to understand how Visual Studio uses this Dockerfile to build your images for faster debugging.

FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
WORKDIR /app
EXPOSE 81
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY ["Kjemidagen.csproj", "."]
RUN dotnet restore "./Kjemidagen.csproj"
COPY . .
WORKDIR "/src/."
RUN dotnet build "Kjemidagen.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "Kjemidagen.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "Kjemidagen.dll"]