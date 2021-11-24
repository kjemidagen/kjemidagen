using System.ComponentModel.DataAnnotations;

namespace Kjemidagen.Models
{
    public class Company: User
    {   
        [Required]
        [DataType(DataType.EmailAddress)]
        public string EmailAddress { get; init; } = string.Empty;
        [Required]
        public string Name {get; init; } = string.Empty;
        public string Information {get; init; } = string.Empty;
        public int NumberOfCompanyRepresentatives { get; init; } = 0;
    }
}