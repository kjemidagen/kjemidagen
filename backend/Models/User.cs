using System.ComponentModel.DataAnnotations;

namespace Kjemidagen.Models
{
    public class User
    {
        public int Id { get; init; }

        [Required]
        public string Username { get; init; } = string.Empty;

        [Required]
        public string HashedPassword { get; init; } = string.Empty;
        public bool IsAdmin { get; init; } = false;
        public bool IsCompany { get; init; } = false;
    }
}