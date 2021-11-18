using System.ComponentModel.DataAnnotations;

namespace Kjemidagen.Models
{
    public class Company
    {
        public int ID;
        [Required]
        [DataType(DataType.EmailAddress)]
        public string EmailAddress { get; set; } = string.Empty;
        [Required]
        public string HashedPassword {get; set; } = string.Empty;
        [Required]
        public string Name {get; set; } = string.Empty;
        public string Information {get; set; } = string.Empty;
        public int NumberOfCompanyRepresentatives { get; set; } = 0;
    }
}