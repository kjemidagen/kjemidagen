using System.ComponentModel.DataAnnotations;

namespace Kjemidagen.Models
{
    public class RefreshToken
    {
        [Key]
        public string TokenString { set; get; } = null!;
        public User Owner { set; get; } = null!;
        public int UserId { set; get; }
    }
} 