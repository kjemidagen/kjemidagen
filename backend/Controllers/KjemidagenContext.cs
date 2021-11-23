using Microsoft.EntityFrameworkCore;

namespace Kjemidagen.Models
{
    public class KjemidagenContext : DbContext
    {
        public KjemidagenContext(DbContextOptions<KjemidagenContext> options) 
            : base(options) 
        {
        }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        => optionsBuilder
            .UseNpgsql(@"Host=localhost;Port=5432;Username=admin;Password=kjemidagen;Database=kjemidagen");

        public DbSet<Company> Companies { get; set; } = null!;
    }
}