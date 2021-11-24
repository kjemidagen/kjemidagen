using Microsoft.EntityFrameworkCore;

namespace Kjemidagen.Models
{
    public class KjemidagenContext : DbContext
    {
        public KjemidagenContext(DbContextOptions<KjemidagenContext> options) 
            : base(options) 
        {}

        public DbSet<User> Users { get; set; } = null!;
        public DbSet<Company> Companies { get; set; } = null!;
        public DbSet<RefreshToken> RefreshTokens { get; set; } = null!;
    }
}